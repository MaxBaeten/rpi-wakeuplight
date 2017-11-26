<html>
<head>
    <meta name="viewport" content="width=device-width" />
    <title>Submitting Wecker Form</title>
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
        
        // Fetch current sql values
        $resmon = $conn->query("SELECT * FROM Wecker.Settings WHERE day='monday'")->fetch_assoc();
        $restue = $conn->query("SELECT * FROM Wecker.Settings WHERE day='tuesday'")->fetch_assoc();
        $reswed = $conn->query("SELECT * FROM Wecker.Settings WHERE day='wednesday'")->fetch_assoc();
        $resthu = $conn->query("SELECT * FROM Wecker.Settings WHERE day='thursday'")->fetch_assoc();
        $resfri = $conn->query("SELECT * FROM Wecker.Settings WHERE day='friday'")->fetch_assoc();
        $ressat = $conn->query("SELECT * FROM Wecker.Settings WHERE day='saturday'")->fetch_assoc();
        $ressun = $conn->query("SELECT * FROM Wecker.Settings WHERE day='sunday'")->fetch_assoc();
        
        // Update time in SQL database if time has changed
        if ($resmon['time'] != $_POST['monday_time'] ) {
            $conn->query("UPDATE Wecker.Settings SET time = '0000-00-00 ". $_POST['monday_time']. ":00' WHERE day = 'monday';");
        }
        if ($restue['time'] != $_POST['tuesday_time'] ) {
            $conn->query("UPDATE Wecker.Settings SET time = '0000-00-00 ". $_POST['tuesday_time']. ":00' WHERE day = 'tuesday';");
        }
        if ($reswed['time'] != $_POST['wednesday_time'] ) {
            $conn->query("UPDATE Wecker.Settings SET time = '0000-00-00 ". $_POST['wednesday_time']. ":00' WHERE day = 'wednesday';");
        }
        if ($resthu['time'] != $_POST['thursday_time'] ) {
            $conn->query("UPDATE Wecker.Settings SET time = '0000-00-00 ". $_POST['thursday_time']. ":00' WHERE day = 'thursday';");
        }
        if ($resfri['time'] != $_POST['friday_time'] ) {
            $conn->query("UPDATE Wecker.Settings SET time = '0000-00-00 ". $_POST['friday_time']. ":00' WHERE day = 'friday';");
        }
        if ($ressat['time'] != $_POST['saturday_time'] ) {
            $conn->query("UPDATE Wecker.Settings SET time = '0000-00-00 ". $_POST['saturday_time']. ":00' WHERE day = 'saturday';");
        }
        if ($ressun['time'] != $_POST['sunday_time'] ) {
            $conn->query("UPDATE Wecker.Settings SET time = '0000-00-00 ". $_POST['sunday_time']. ":00' WHERE day = 'sunday';");
        }
        
        // Fetch current check box values of the GUI
        if(isset($_POST['enablemon']) && $_POST['enablemon'] == 'Yes') {
            $enablemon = 1;
        } else {
            $enablemon = 0;
        }
        if(isset($_POST['enabletue']) && $_POST['enabletue'] == 'Yes') {
            $enabletue = 1;
        } else {
            $enabletue = 0;
        }
        if(isset($_POST['enablewed']) && $_POST['enablewed'] == 'Yes') {
            $enablewed = 1;
        } else {
            $enablewed = 0;
        }
        if(isset($_POST['enablethu']) && $_POST['enablethu'] == 'Yes') {
            $enablethu = 1;
        } else {
            $enablethu = 0;
        }
        if(isset($_POST['enablefri']) && $_POST['enablefri'] == 'Yes') {
            $enablefri = 1;
        } else {
            $enablefri = 0;
        }
        if(isset($_POST['enablesat']) && $_POST['enablesat'] == 'Yes') {
            $enablesat = 1;
        } else {
            $enablesat = 0;
        }
        if(isset($_POST['enablesun']) && $_POST['enablesun'] == 'Yes') {
            $enablesun = 1;
        } else {
            $enablesun = 0;
        }
        
        // Update enable in SQL database if enable has changed
        if ($resmon['enable'] != $enablemon) {
            $conn->query("UPDATE Wecker.Settings SET enable = ". $enablemon. " WHERE day = 'monday';");
        }
        if ($restue['enable'] != $enabletue) {
            $conn->query("UPDATE Wecker.Settings SET enable = ". $enabletue. " WHERE day = 'tuesday';");
        }
        if ($reswed['enable'] != $enablewed) {
            $conn->query("UPDATE Wecker.Settings SET enable = ". $enablewed. " WHERE day = 'wednesday';");
        }
        if ($resthu['enable'] != $enablethu) {
            $conn->query("UPDATE Wecker.Settings SET enable = ". $enablethu. " WHERE day = 'thursday';");
        }
        if ($resfri['enable'] != $enablefri) {
            $conn->query("UPDATE Wecker.Settings SET enable = ". $enablefri. " WHERE day = 'friday';");
        }
        if ($ressat['enable'] != $enablesat) {
            $conn->query("UPDATE Wecker.Settings SET enable = ". $enablesat. " WHERE day = 'saturday';");
        }
        if ($ressun['enable'] != $enablesun) {
            $conn->query("UPDATE Wecker.Settings SET enable = ". $enablesun. " WHERE day = 'sunday';");
        }
    
    ?>
    
    <form action="index.php" method="post">
        <input type="submit" name="return" value="return" />
    </form>
    
</body>
</html>
