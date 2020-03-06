<!DOCTYPE html>
<html>
<head>
    <title>Ghost Riders</title>
    <style>
        table {
            border-collapse:collapse;
            width: 100%;
            color: #588c7e 
            font-family: monospace;
            font-size: 25px;
            text-align: center;
            }
        th {
            background_color: #588c7e
            color:white;
            
        }
        tr:nth-child(even) {
            background-color: #f2f2f2
        }
    </style>
</head>
<body>
<table>
    <tr>
        <th>subject id</th>
        <th>age</th>
        <th>gender</th>
    </tr>
    <?php
    $conn = mysqli_connect("127.0.0.1", "root", "12345678", "GhostRiders");
    if ($conn-> connect_error) {
        die("Connection failed:". $conn-> connect_error);
    }
    $sql = "SELECT subject_id, age, gender from Subjects";
    $result = $conn-> query($sql);
    if($result-> num_rows > 0) {
        while ($row = $result -> fetch_assoc()){
            echo "<tr><td>". $row["subject_id"]."</td><td>". $row["age"]. "</td><td>". $row["gender"]. "</td><td>";
        }
        echo"</table>";
    }
    else {
        echo "0 result";
    }
    $conn -> close(); 
    ?>
</table>
</body>
</html>
