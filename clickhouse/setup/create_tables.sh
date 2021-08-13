clickhouse-client -u default --password=bPt0Y/GIB7oxsJX9 --query="CREATE TABLE IF NOT EXISTS default.gastos
(
	motivo String,
	cantidad Float32,
	categoria String,
	necesario UInt8,
	fecha Date
)
ENGINE = TinyLog();"

clickhouse-client -u default --password=bPt0Y/GIB7oxsJX9 --query="CREATE TABLE IF NOT EXISTS default.bascula
(
	grasa_corporal Float32,
	agua Float32,
	proteina Float32,
	metabolismo_basal UInt32,
	grasa_visceral UInt32,
	musculo Float32,
	masa_osea Float32,
	peso Float32,
	fecha Date
)
ENGINE = TinyLog();"