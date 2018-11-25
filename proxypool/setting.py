# Redis 设置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = "proxies"

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

# 代理池上限
POOL_UPPER_THRESHOLD = 10000

# 可行状态码
VALID_STATUS_CODES = [200, 302]

# 检查周期
TESTER_CYCLE = 20

# 获取周期
GETTER_CYCLE = 20

# 功能开关
TESTER_ENABLED = False
API_ENABLED = True
GETTER_ENABLED = False

# 接口设置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 测试url
TEST_URL = 'http://www.baidu.com'
# 测试批量
BATCH_TEST_SIZE = 100
