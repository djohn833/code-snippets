<?php


$mysqli = new mysqli("127.0.0.1", "sql_injection", "", "sql_injection");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
    die();
}
echo $mysqli->host_info . "\n";

$username = $argv[1];
$password = $argv[2];

$sql = "SELECT id, username FROM users WHERE username='" . $username . "' AND password='" . $password . "'";

echo $sql . "\n";
echo "\n";

$res = $mysqli->query($sql);

while ($row = $res->fetch_assoc()) {
    echo "id = " . $row['id'] . ", username = " . $row['username'] . "\n";
}

?>
