# WOAN_GYM

自研机器狗（4310电机）强化学习训练框架，基于 IsaacGym。

## 一、环境搭建

### 拉取代码仓库

```bash
git clone https://github.com/XUEHAIXU/WOAN_GYM.git
```

### 创建 conda 环境

```bash
conda create -n woan4310 python=3.8
conda activate woan4310
```

### 安装 IsaacGym

官网下载安装包：https://developer.nvidia.com/isaac-gym/download

```bash
tar -xvf IsaacGym_Preview_4_Package.tar.gz
cd isaacgym/python
pip install -e .
```

### 安装 rsl-rl 算法库

```bash
cd rsl_rl
pip install -e .
```

### 安装 WOAN_GYM

```bash
cd WOAN_GYM
pip install -e .
```

### 设置环境变量

```bash
export PYTHONPATH=/你的isaacgym路径/isaacgym/python:$PYTHONPATH
export PYTHONPATH=/你的rsl_rl路径:$PYTHONPATH
```

### 常见问题

若出现 `numpy` 报错：

```
AttributeError: module 'numpy' has no attribute 'float'.
```

修改 isaacgym/torch_utils.py：

```bash
sed -i 's/np\.float/float/g' /你的isaacgym路径/isaacgym/python/isaacgym/torch_utils.py
```

## 二、训练

训练（关闭可视化）：

```bash
python legged_gym/scripts/train.py --task=woan4310 --headless
```

训练完成后，查看训练成果：

```bash
python legged_gym/scripts/play.py --task=woan4310
```

训练过程中可以使用 tensorboard 查看数据。

## 项目结构

```
legged_gym/
├── envs/
│   ├── base/                          # 核心底层逻辑
│   │   ├── base_config.py             # 全局配置模板（环境数、设备等）
│   │   ├── base_task.py               # 仿真器接口（Step, Reset 实现）
│   │   ├── legged_robot.py            # 机器人物理逻辑（传感器、物理驱动、奖励计算）
│   │   └── legged_robot_config.py     # 机器人默认配置（默认PID、默认奖励权重）
│   └── WOAN4310_MoB/WOAN4310_Trot/    # 4310机器狗任务特化
│       ├── WOAN4310_config.py
│       └── WOAN4310.py
└── scripts/
    ├── train.py                       # 训练启动脚本
    └── play.py                        # 验证与导出脚本
```
