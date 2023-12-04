<?php

require_once('../helpers.php');

function first()
{
    $arr = toLines("input.txt");

    $finalArray = array_map(function ($line) {
        $first_digit = -1;
        $second_digit = -1;
        foreach (str_split($line) as $char) {
            if (is_numeric($char)) {
                if ($first_digit < 0) {
                    $first_digit = $char;
                }
                else {
                    $second_digit = $char;
                }
            }
        }
        if ($second_digit < 0) {
            $second_digit = $first_digit;
        }
        return intval($first_digit . $second_digit);
    }, $arr);

    echo array_sum($finalArray);
}

function second()
{
    $arr = toLines("input.txt");
    $digits = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    ];
    $values = [
        'one' => '1',
        'two' => '2',
        'three' => '3',
        'four' => '4',
        'five' => '5',
        'six' => '6',
        'seven' => '7',
        'eight' => '8',
        'nine' => '9',
    ];

    $finalArray = array_map(function ($line) use ($digits, $values) {
        $strpos = [];

        foreach ($digits as $digit) {
            if (strpos($line, $digit) !== false) {
                $strpos[$digit] = strpos($line, $digit);
            }
        }

        asort($strpos);
        $first_digit = is_numeric(key($strpos)) ? key($strpos) : $values[key($strpos)];

        $strpos = [];
        
        foreach ($digits as $digit) {
            $lastPos = 0;
            while (($lastPos = strpos($line, $digit, $lastPos)) !== false) {
                $strpos[$digit] = $lastPos;
                $lastPos = $lastPos + strlen($digit);
            }
        }
        arsort($strpos, SORT_DESC);
        $second_digit = is_numeric(key($strpos)) ? key($strpos) : $values[key($strpos)];

        return intval($first_digit . $second_digit);
    }, $arr);

    echo array_sum($finalArray);
}

first();
echo '<br>';
second();
