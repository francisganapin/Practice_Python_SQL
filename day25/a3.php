<?php
$loggedIn = true;
$isAdmin = true;


if($loggedIn){
    if($isAdmin){
        echo 'Welcome,Admin';
    }else {
        echo "Welcome,User";
    }
}else {
    echo 'Please log in.';
}

?>