<html>
<head>
    <meta name="viewport" content="width=device-width" />
    <title>Wecker by Max</title>

    <style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }

    </style>
</head>

<body>
    <?php
        include 'sqlparam.php';

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        
        // Monday Query
        $result = $conn->query("SELECT * FROM Wecker.Settings WHERE day='monday'");
        $resmon = $result->fetch_assoc();

        // Tuesday Query
        $result = $conn->query("SELECT * FROM Wecker.Settings WHERE day='tuesday'");
        $restue = $result->fetch_assoc();

        // Wednesday Query
        $result = $conn->query("SELECT * FROM Wecker.Settings WHERE day='wednesday'");
        $reswed = $result->fetch_assoc();

        // Thursday Query
        $result = $conn->query("SELECT * FROM Wecker.Settings WHERE day='thursday'");
        $resthu = $result->fetch_assoc();

        // Friday Query
        $result = $conn->query("SELECT * FROM Wecker.Settings WHERE day='friday'");
        $resfri = $result->fetch_assoc();

        // Saturday Query
        $result = $conn->query("SELECT * FROM Wecker.Settings WHERE day='saturday'");
        $ressat = $result->fetch_assoc();

        // Sunday Query
        $result = $conn->query("SELECT * FROM Wecker.Settings WHERE day='sunday'");
        $ressun = $result->fetch_assoc();

    ?>
    
    <form action="submitform.php" method="post">
        
        <table>
            <tr>
                <th>Day</th>
                <th>Enable</th>
                <th>Time</th>
            </tr>
            <tr>
                <td> Monday </td>
                <?php 
                    if ($resmon["enable"]) {
                        echo "<td> <input type='checkbox' name='enablemon' value='Yes' checked=checked /> </td> \r\n";
                    } else {
                        echo "<td> <input type='checkbox' name='enablemon' value='Yes' /> </td> \r\n";
                    } 
                ?>
                <?php
                    echo "<td> <input type='time' name='monday_time' value='", substr($resmon['time'],0,5), "'/> </td> \r\n";
                ?>
            </tr>
            <tr>
                <td> Thuesday </td>
                <?php 
                    if ($restue["enable"]) {
                        echo "<td> <input type='checkbox' name='enabletue' value='Yes' checked=checked /> </td> \r\n";
                    } else {
                        echo "<td> <input type='checkbox' name='enabletue' value='Yes' /> </td> \r\n";
                    } 
                ?>
                <?php
                    echo "<td> <input type='time' name='tuesday_time' value='", substr($restue['time'],0,5), "'/> </td> \r\n";
                ?>
            </tr>
            <tr>
                <td> Wednesday </td>
                <?php 
                    if ($reswed["enable"]) {
                        echo "<td> <input type='checkbox' name='enablewed' value='Yes' checked=checked /> </td> \r\n";
                    } else {
                        echo "<td> <input type='checkbox' name='enablewed' value='Yes' /> </td> \r\n";
                    } 
                ?>
                <?php
                    echo "<td> <input type='time' name='wednesday_time' value='", substr($reswed['time'],0,5), "'/> </td> \r\n";
                ?>
            </tr>
            <tr>
                <td> Thursday </td>
                <?php 
                    if ($resthu["enable"]) {
                        echo "<td> <input type='checkbox' name='enablethu' value='Yes' checked=checked /> </td> \r\n";
                    } else {
                        echo "<td> <input type='checkbox' name='enablethu' value='Yes' /> </td> \r\n";
                    } 
                ?>
                <?php
                    echo "<td> <input type='time' name='thursday_time' value='", substr($resthu['time'],0,5), "'/> </td> \r\n";
                ?>
            </tr>
            <tr>
                <td> Friday </td>
                <?php 
                    if ($resfri["enable"]) {
                        echo "<td> <input type='checkbox' name='enablefri' value='Yes' checked=checked /> </td> \r\n";
                    } else {
                        echo "<td> <input type='checkbox' name='enablefri' value='Yes' /> </td> \r\n";
                    } 
                ?>
                <?php
                    echo "<td> <input type='time' name='friday_time' value='", substr($resfri['time'],0,5), "'/> </td> \r\n";
                ?>
            </tr>
            <tr>
                <td> Saturday </td>
                <?php 
                    if ($ressat["enable"]) {
                        echo "<td> <input type='checkbox' name='enablesat' value='Yes' checked=checked /> </td> \r\n";
                    } else {
                        echo "<td> <input type='checkbox' name='enablesat' value='Yes' /> </td> \r\n";
                    }
                ?>
                <?php
                    echo "<td> <input type='time' name='saturday_time' value='", substr($ressat['time'],0,5), "'/> </td> \r\n";
                ?>
            </tr>
            <tr>
                <td> Sunday </td>
                <?php 
                    if ($ressun["enable"]) {
                        echo "<td> <input type='checkbox' name='enablesun' value='Yes' checked=checked /> </td> \r\n";
                    } else {
                        echo "<td> <input type='checkbox' name='enablesun' value='Yes' /> </td> \r\n";
                    }
                ?>
                <?php
                    echo "<td> <input type='time' name='sunday_time' value='", substr($ressun['time'],0,5), "'/> </td> \r\n";
                ?>
            </tr>
        </table>
        
        <input type="submit" name="submitform" value="Submit" />

    </form>
</body>
</html>
