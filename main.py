import hydra
#from omegaconf import DictConfig, OmegaConf
#import flatdict
from omegaconf import MISSING
from dataclasses import dataclass
from hydra.core.config_store import ConfigStore

@dataclass
class Files:
    data: str = MISSING
    log: str = MISSING

    def __post_init__(self):
        print("Initialised Files") 
        print(self.data)
    
@dataclass
class Params:
    x: int = 0
    y: int = 0

    def __post_init__(self):
        print("Initialised Params") 
    
@dataclass
class ThisConfig:
    files: Files = Files()
    params: Params = Params()

    def __post_init__(self):
        print("Initialised ThisConfig")
        print("Files", self.files)


cs = ConfigStore.instance()
cs.store(name='xxx', node=ThisConfig)

@hydra.main(version_base=None, config_path="conf",config_name = "top_config")
def main(cfg: ThisConfig):
    cfg = ThisConfig(**cfg)
    print(cfg)
    print(cfg.files.__dict__)
    print(cfg.files)
    print(cfg.params)
    print(type(cfg))
    """
    x = OmegaConf.to_yaml(cfg)
    print(x)
    
    original_wd = hydra.utils.get_original_cwd()
    print(original_wd)
    
    hparam_dict = OmegaConf.to_container(cfg, resolve=True)
    print(hparam_dict)
    
    hparam_dict = dict(flatdict.FlatterDict(hparam_dict, delimiter='.'))
    print(hparam_dict)
    """
    return

if __name__ == "__main__":
    main()
