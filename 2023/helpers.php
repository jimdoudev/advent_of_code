<?php

function toLines($input)
{
    $lines = [];
    $file = fopen($input, "r") or die("Unable to open file!");
    while (!feof($file)) {
        $line = rtrim(fgets($file));
        if (!empty($line)) {
            $lines[] = $line;
        }
    }
    fclose($file);
    return $lines;
}
