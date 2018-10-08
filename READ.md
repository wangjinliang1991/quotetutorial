# scrapy项目quotetutorial

## 使用Item Pipeline
* 清理HTML数据
* 验证爬取数据，检查爬取字段
* 查重并丢弃重复内容
* 将爬取结果保存到数据库

## settings设置
* 赋值ITEM_PIPELINE字典，键名是PIpeline的类名称，键值是调用优先级，数字越小越先被调用