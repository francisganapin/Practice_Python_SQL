<?php

    $rows = [
        ['name' => 'Phone','Stock' => 12],
        ['name' => 'Laptop','Stock' => 0 ],
        ['name' => 'Mouse','Stock' => 8],
    ];

    foreach ($rows as $row) {
        if ($row['stock'] == 0) {
            echo "{$row['name']} is out of stock\n";
        }
    }
    

    ?>