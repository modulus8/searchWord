<html>
<head>
	<title>シンプル英単語検索</title>
	<style>
		body{ margin-left: auto; margin-right: auto; width:70%;}
		input{font-size:18px;}
		audio{width:90%;}
		.example_list{font-size: 14px;}
	</style>
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<hr>
<form action="/" method="get">
	<div><input id="word" type="text" name="word" value="{{word}}" autofocus></div>


<hr>
<p>
	<strong>[W]:</strong>
	<span>{{weblio.title}}</span>
	<strong>[O]:</strong>
	<span>{{oxford.title}}</span>
</p>
<p><span>[pronounce]:</span>{{oxford.pronounce}}</p>
<p>
	<span>{{weblio.translation}}<br /></span>
	<span>{{weblio.others}}<br /></span>
	<span>{{weblio.prediction_all}}<br /></span>
</p>
<audio controls="controls" onended="window.focus()">
	<source src="{{oxford.mp3}}" type="audio/mpeg">
</audio>

<hr>
	<div>
		<button type="submit">検索</button>
		<button type="button" onclick="window.reset()">リセット</button>
	</div>
</form>

<hr>
<div>
	<ul>
		% for sentence in weblio.example:
			<li class="example_list">{{sentence}}</li>
		% end
	</ul>
</div>
<script>
	function reset(){
		document.getElementById('word').value="";
		window.focus();
	}
	
	function focus(){
		document.getElementById('word').focus();
	}

</script>
</body>
</html>
