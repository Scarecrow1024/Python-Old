<?php

function post_requst( $end_point, $params) {
  $ch = curl_init( $end_point );
  curl_setopt( $ch, CURLOPT_POST, 1);
  curl_setopt( $ch, CURLOPT_POSTFIELDS, $params);
  curl_setopt( $ch, CURLOPT_FOLLOWLOCATION, 1);
  curl_setopt( $ch, CURLOPT_HEADER, 0);
  curl_setopt( $ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt ($ch, CURLOPT_SSL_VERIFYHOST, 0);
  curl_setopt ($ch, CURLOPT_SSL_VERIFYPEER, 0); 
  $response = curl_exec( $ch );
  curl_close ($ch);
  return $response;
}

# 获得email帐号(username)和密码(password) ,需要到这里注册 http://chongdata.com/old/register.php
$username = "xxx@xxx.com";
$password = "xxxx";
$root = 'https://www.chongdata.com/ocr/dev_api_v2';
$end_point_submit_job = $root.'/submit_job.php';
$end_point_job_status = $root.'/job_status.php';
$end_point_get_res = $root.'/get_res.php';


# Recognize a file from local disk
## 本地文件识别
$file_name_with_full_path = realpath('./sample1.png');
# Mixing chinese and english
# 英语: en， 简体中文: cn_sim， 繁体中文: cn_tr 可以混合语言
$params = array('langs[0]' => "cn_sim",
	        'langs[1]' => "en",
	        'username' => $username,
	        'password' => $password,
	        'file'=>'@'.$file_name_with_full_path);

# Submit a job
# 提交任务到服务器
$from_time = time();
$job_id = post_requst($end_point_submit_job, $params);

echo $job_id."\n";

if(strpos($job_id,'error') !== false)
{
  echo "提交失败"."\n";
  exit();
}


$params = array('job_id' => $job_id);

# 任务状态只有Doing和Done
do
{
  $job_status = post_requst($end_point_job_status, $params);
  echo $job_status."\n";
  sleep(3);
}while(strpos($job_status,'Doing') !== false);
$to_time = time();
echo "识别时间: ".abs($to_time - $from_time)." 秒.";

$res = post_requst($end_point_get_res, $params);
echo "识别结果:"."\n";
echo $res."\n";

?>
