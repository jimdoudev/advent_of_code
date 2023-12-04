<?php

function toLines($input)
{
    $lines = [];
    $file = fopen($input, "r") or die("Unable to open file!");
    while (!feof($file)) {
        $lines[] = rtrim(fgets($file));
    }
    fclose($file);
    return $lines;
}
