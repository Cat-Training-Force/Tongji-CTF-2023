<?php

error_reporting(0);
show_source(__FILE__);

$a = $_GET["a"];
$b = $_GET["b"];
$c = $_GET["c"];
$d = $_GET["d"];
$e = $_GET["e"];
$f = $_GET["f"];
$g = $_GET["g"];

if(preg_match("/Error|ArrayIterator|SplFileObject/i", $a)) {
    die("什么原生类，我不懂啊");
}


if(preg_match("/php/i", $b)) {
 die("根本用不上");
}

if(preg_match("/Error|ArrayIterator/i", $c)) {
 die("现在是，幻想时间");
}


$class = new $a($b);
$str1 = substr($class->$c(),$d,$e);
$str2 = substr($class->$c(),$f,$g);
$str1($str2);