<?php

require_once('../helpers.php');

function first()
{
    $limits = [
        'red' => 12,
        'green' => 13,
        'blue' => 14,
    ];

    $lines = toLines("input.txt");

    $rounds = [];
    foreach ($lines as $line) {
        $splitLine = explode(":", $line);
        $id = explode(" ", $splitLine[0])[1];
        $games = explode(";", $splitLine[1]);

        $splitGames = array_map(function ($game) {
            $splitGame = array_map(function ($count) {
                return explode(" ", trim($count));
            }, explode(",", $game));

            return $splitGame;
        }, $games);

        $rounds[$id] = $splitGames;
    };

    foreach ($rounds as $id => $games) {
        $results = array_map(function ($colors) use ($limits) {
            foreach ($colors as $color) {
                if ($color[0] > $limits[$color[1]]) {
                    return 0;
                }
            }
            return 1;
        }, $games);
        $rounds[$id] = array_sum($results) < count($results) ? 0 : 1;
    }

    $possible_games = [];
    foreach ($rounds as $id => $possible) {
        if ($possible) {
            $possible_games[] = $id;
        }
    }

    echo array_sum($possible_games);
}

function second()
{
    $lines = toLines("input.txt");

    $rounds = [];
    $powers = [];
    foreach ($lines as $line) {
        $splitLine = explode(":", $line);
        $id = explode(" ", $splitLine[0])[1];
        $games = explode(";", $splitLine[1]);

        $splitGames = array_map(function ($game) {
            $splitGame = array_map(function ($count) {
                return explode(" ", trim($count));
            }, explode(",", $game));

            return $splitGame;
        }, $games);

        $rounds[$id] = $splitGames;
    };

    foreach ($rounds as $id => $games) {
        $max_color = [
            'red' => 0,
            'green' => 0,
            'blue' => 0,
        ];
        foreach ($games as $game) {
            foreach ($game as $color) {
                if ($color[0] > $max_color[$color[1]]) {
                    $max_color[$color[1]] = $color[0];
                }
            }
        };
        $powers[] = $max_color['red'] * $max_color['green'] * $max_color['blue'];
    }

    echo array_sum($powers);
}

first();
echo '<br>';
second();
