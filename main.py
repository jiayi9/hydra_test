import hydra
#from omegaconf import DictConfig, OmegaConf
#import flatdict

from dataclasses import dataclass
from hydra.core.config_store import ConfigStore

@dataclass
class Files:
    data: str
    log: str
    
@dataclass
class Params:
    x: int
    y: int
    
@dataclass
class ThisConfig:
    files: Files
    params: Params

cs = ConfigStore.instance()
cs.store(name='xxx', node=ThisConfig)

@hydra.main(version_base=None, config_path="conf",config_name = "config")
def main(cfg: ThisConfig):
    print(cfg)
    print(cfg.files)
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

main()
