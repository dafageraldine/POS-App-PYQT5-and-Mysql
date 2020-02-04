CREATE DATABASE bullEyeArchery;
USE bullEyeArchery;

CREATE TABLE `admin` (
  `id` tinyint(4) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

LOCK TABLES `admin` WRITE;
INSERT INTO `admin` VALUES (1,'admin','1234');
INSERT INTO `admin` VALUES (2,'master', '0123');
UNLOCK TABLES;

CREATE TABLE `ads` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `daftarbarang` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idProduk` varchar(20) DEFAULT NULL,
  `nama` text,
  `kategori` varchar(20) DEFAULT NULL,
  `foto` text,
  `harga` int(11) DEFAULT '0',
  `hpp` int(11) DEFAULT '0',
  `stock` smallint(6) DEFAULT '0',
  `diskon` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`)
);

CREATE TABLE `ipline` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ipAddress` varchar(15) DEFAULT NULL,
  `line` varchar(10) DEFAULT NULL,
  `available` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

LOCK TABLES `ipline` WRITE;
/*!40000 ALTER TABLE `ipline` DISABLE KEYS */;
INSERT INTO `ipline` VALUES (19,'192.168.1.123','Line 1',1),(20,'192.168.1.145','Line 2',1),(21,'192.168.100.1','Line 3',1),(24,'192.168.1.190','Line 4',1),(25,'','Line 5',0),(26,'','Line 6',0),(27,'','Line 7',0),(28,'','Line 8',0),(29,'','Line 9',0),(30,'','Line 10',0),(31,'','Line 11',0),(32,'','Line 12',0),(33,'','Line 13',0),(34,'','Line 14',0),(35,'','Line 15',0),(36,'','Line 16',0),(37,'','Line 17',0),(38,'','Line 18',0),(39,'','Line 19',0),(40,'','Line 20',0);
/*!40000 ALTER TABLE `ipline` ENABLE KEYS */;
UNLOCK TABLES;

CREATE TABLE `pelanggan` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idPelanggan` varchar(255) DEFAULT NULL,
  `rfid` varchar(20) DEFAULT NULL,
  `nama` text,
  `gender` varchar(12) DEFAULT NULL,
  `member` varchar(10) DEFAULT NULL,
  `alamat` text,
  `kontak` varchar(15) DEFAULT NULL,
  `foto` text,
  `saldo` int(10) unsigned DEFAULT '0',
  `point` int(11) DEFAULT '0',
  `line` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `pengeluaran` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `struk` text,
  `nama` text,
  `harga` int(11) DEFAULT NULL,
  `jumlah` tinyint(4) DEFAULT NULL,
  `diskon` tinyint(4) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  `waktu` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE `setting` (
  `idSettings` varchar(45) NOT NULL,
  `camera` int(11) DEFAULT NULL,
  `batasbawah` int(11) DEFAULT NULL,
  `batastengah` int(11) DEFAULT NULL,
  `batasatas` int(11) DEFAULT NULL,
  PRIMARY KEY (`idSettings`)
);

LOCK TABLES `setting` WRITE;
INSERT INTO `setting` VALUES ('set-1',0,100,250,300);
UNLOCK TABLES;

CREATE TABLE `stock` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idProduk` varchar(20) DEFAULT NULL,
  `nama` text,
  `jumlah` smallint(6) DEFAULT NULL,
  `waktu` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE `transaksi` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `idTransaksi` varchar(20) DEFAULT NULL,
  `idProduk` varchar(20) DEFAULT NULL,
  `produk` text,
  `harga` int(11) DEFAULT NULL,
  `jumlah` tinyint(4) DEFAULT NULL,
  `total` int(10) unsigned DEFAULT NULL,
  `idPelanggan` varchar(255) DEFAULT NULL,
  `pelanggan` text,
  `jenisTransaksi` varchar(10) DEFAULT NULL,
  `line` varchar(2) DEFAULT NULL,
  `waktu` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);
