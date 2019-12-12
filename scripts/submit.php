function submit($part, $answer)
{
	$response = [];
	
	exec("./submit $part $answer", $response);
	
	return $response[0];
}