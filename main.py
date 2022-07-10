import hydra
from omegaconf import DictConfig, OmegaConf
import flatdict
import albumentations as A
from albumentations.pytorch import ToTensorV2
from albumentations import (OneOf, Resize, Normalize, Compose, Transpose, HorizontalFlip, VerticalFlip,
                            Cutout, ShiftScaleRotate, GaussianBlur, RandomBrightness, Sharpen, RandomCrop)

@hydra.main(version_base=None, config_path="conf",config_name = "config")
def main(cfg):
    #print(cfg)

    print(type(cfg))
    
    transforms = []

    for aug_cfg in cfg['train_aug']:
        print(aug_cfg)
        print(aug_cfg.trans_func_name)
        params = OmegaConf.to_container(aug_cfg.params,
                                        resolve=True)
        print(params)
        transforms.append(
            getattr(A, aug_cfg.trans_func_name)(**params)
        )

    transforms.append(ToTensorV2())
    
    print(transforms)
    
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
