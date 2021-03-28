<h1>XSS Test Playground</h1>

Use the GET parameter to play with different contexts:<br />
'a': normal PHP echo<br />
'aa': htmlspecialchars() echo (without ENT_QUOTES)<br />

<br />
<br />
<b><a href="?a=xss">$_GET['a']</a> | <a href="?aa=xss">$_GET['aa']</a> - HTML context</b>:<br />
a: <?php if (isset($_GET['a'])) { echo $_GET['a']; } ?><br />
aa: <?php if (isset($_GET['aa'])) { echo htmlspecialchars($_GET['aa']); } ?><br />

<br />
<br />
<b><a href="?b=xss">$_GET['b']</a> | <a href="?bb=xss">$_GET['bb']</a> | <a href="?bbb=xss">$_GET['bbb']</a> - HTML attribute context</b> in quotes:<br />
b: <img src="<?php if (isset($_GET['b'])) {echo $_GET['b']; } ?>"><br />
bb: <img src="<?php if (isset($_GET['bb'])) {echo htmlspecialchars($_GET['bb']); } ?>"><br />
bbb: <img src='<?php if (isset($_GET['bbb'])) {echo htmlspecialchars($_GET['bbb']); } ?>'><br />

<br />
<br />
<b><a href="?c=xss">$_GET['c']</a> | <a href="?cc=xss">$_GET['cc']</a> - HTML attribute context</b> no quotes:<br />
c: <img src=<?php if (isset($_GET['c'])) {echo $_GET['c']; } ?>><br />
cc: <img src=<?php if (isset($_GET['cc'])) {echo htmlspecialchars($_GET['cc']); } ?>><br />

<br />
<br />
<b><a href="?d=xss">$_GET['d']</a> | <a href="?dd=xss">$_GET['dd']</a> - Script context</b>:<br />
d: <script><?php if (isset($_GET['d'])) {echo $_GET['d']; } ?></script><br />
dd: <script><?php if (isset($_GET['dd'])) {echo htmlspecialchars($_GET['dd']); } ?></script><br />

