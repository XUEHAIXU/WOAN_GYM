from legged_gym import LEGGED_GYM_ROOT_DIR, LEGGED_GYM_ENVS_DIR

from legged_gym.envs.WOAN4310_MoB.WOAN4310_Trot.WOAN4310 import WOAN4310_Robot
from legged_gym.envs.WOAN4310_MoB.WOAN4310_Trot.WOAN4310_config import WOAN4310_Cfg_Yu,WOAN4310_PPO_Yu

from legged_gym.utils.task_registry import task_registry

task_registry.register( "woan4310", WOAN4310_Robot, WOAN4310_Cfg_Yu(), WOAN4310_PPO_Yu())

print("注册的任务:  ",task_registry.task_classes)
