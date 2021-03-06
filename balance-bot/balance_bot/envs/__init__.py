from balance_bot.envs.balancebot_env import BalancebotEnv


def __init__(self):
    self._observation = []
    self.action_space = spaces.Discrete(9)
    # pitch, gyro, commanded speed
    self.observation_space = spaces.Box(np.array([-math.pi, -math.pi, -5]),
                                        np.array([math.pi, math.pi, 5]))
    self.physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # used by loadURDF
    self._seed()
