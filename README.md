# Unauthorized
批量检测未授权情况
使用方法：
	将需要扫描的ip放入hosts.txt里，扫描成功的将被写入success.txt，点击success.txt进行查看。
	使用前需要先安装requirements.txt依赖   requirements.txt pip install

	运行python Unauthorized.py即可

脚本扫描范围：
	redis未授权，默认6379端口
	mongoDB未授权，默认27017端口
	FTP未授权，默认21端口
	zookeeper未授权，默认2181端口
	Elasticsearch未授权，默认9200端口
	Hadoop未授权，默认8088端口
	Kibana未授权，默认80端口
	memcache未授权，默认11211端口
	dockerapi未授权，默认2375端口
	Jenkins未授权，默认8080端口
	CouchDB未授权，默认5984端口
	mysql空口令，默认3306端口
	jboss未授权，默认8080端口
	rsync未授权，默认873端口
	antiveMQ未授权，默认8161端口
	Druid未授权，默认9300端口
	ERLib未授权，默认8099端口
	swaggerapi未授权，默认8080端口
