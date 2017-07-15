<?php

$escape_table = array(
	"\001" => '[.SOH.]',
	"\002" => '[.STX.]',
	"\003" => '[.ETX.]',
	"\004" => '[.EOT.]',
	"\005" => '[.ENQ.]',
	"\006" => '[.ACK.]',
	"\007" => '[.BEL.]',
	"\011" => '[.HT.]',
	"\012" => '[.LF.]',
	"\013" => '[.VT.]',
	"\014" => '[.FF.]',
	"\015" => '[.CR.]',
	"\016" => '[.SO.]',
	"\017" => '[.SI.]',
	"\020" => '[.DLE.]',
	"\021" => '[.DC1.]',
	"\022" => '[.DC2.]',
	"\023" => '[.DC3.]',
	"\024" => '[.DC4.]',
	"\025" => '[.NAK.]',
	"\026" => '[.SYN.]',
	"\027" => '[.ETB.]',
	"\030" => '[.CAN.]',
	"\031" => '[.EM.]',
	"\032" => '[.SUB.]',
	"\033" => '[.ESC.]',
	"\034" => '[.IS4.]',
	"\034" => '[.FS.]',
	"\035" => '[.IS3.]',
	"\035" => '[.GS.]',
	"\036" => '[.IS2.]',
	"\036" => '[.RS.]',
	"\037" => '[.IS1.]',
	"\037" => '[.US.]',
	"\047" => "\\'",
	"\055" => '[.-.]',
	"\134" =>  '\\\\',
	"\135" => '[.].]',
	"\136" => '[.^.]',
	"\177" => '[.DEL.]',
);

function mysql_escape_for_charset($c)
{
	global $escape_table;

	return $escape_table[$c] ?? $c;
}

$mysqli = new mysqli(
    getenv('MYSQL_HOSTNAME'),
    getenv('MYSQL_USERNAME'),
    getenv('MYSQL_PASSWORD'),
    'test');
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
    die();
}
echo $mysqli->host_info . "\n";

// Starting at 1 because MySQL doesn't seem to handle NUL right.
for ($i = 0x01; $i <= 0x7f; $i++) {
	printf("Trying \\%03o (%s)\n", $i, chr($i));

	$pattern = '[' . mysql_escape_for_charset(chr($i)) . ']';

	$sql = "SELECT CHAR($i) REGEXP BINARY '$pattern' AS result";
	$res = $mysqli->query($sql);
	$row = $res->fetch_assoc();
	if ($row['result'] == '0') {
		printf("Escape in single char set did not work for \\%03o (%s)\n", $i, chr($i));
		var_dump($sql);
	}

	$pattern = '[' . mysql_escape_for_charset(chr($i)) . '-' . mysql_escape_for_charset(chr($i)) . ']';

	$sql = "SELECT CHAR($i) REGEXP BINARY '$pattern' AS result";
	$res = $mysqli->query($sql);
	$row = $res->fetch_assoc();
	if ($row['result'] == '0') {
		printf("Escape in char set with range did not work for \\%03o (%s)\n", $i, chr($i));
		var_dump($sql);
	}
}
