<!doctype html>
<title>Results</title>
<head>
<link rel="stylesheet" href="http://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.css" type="text/css" />
<script type="text/javascript" src="http://cdn.pydata.org/bokeh/release/bokeh-0.12.6.min.js"></script>
{{ script | safe }}
</head>

<body>
<a href="http://127.0.0.1:33507/">Back</a><br>
<?php
	// Retrieve the URL variables (using PHP).
	$num = $_POST['stock_ticker'];
	echo "Stock ticker for : ".$num.;
	?>
    </script>
    <div class=page>
        Stock ticker for selected symbol <?php echo $_POST["stock_ticker"]; ?>.
      {{ div | safe }}
    </div>
  </body>
</html>
