<!DOCTYPE html>

<html>

<head>
        <title>Managed Objects Summary</title>
        <meta charset="utf-8" />
		<meta name="author" content="Shashender Kumar" />
        <meta name="description" content="" />
        <style>
            .container{
                margin:0 auto;
                width:85%;
                overflow:auto;
            }
            table.gridtable {
                margin:0 auto;
                width:95%;
                overflow:auto;
                font-family: helvetica,arial,sans-serif;
                font-size:14px;
                color:#333333;
                border-width: 1px;
                border-color: #666666;
                border-collapse: collapse;
                text-align: left;
            }
            table.gridtable th {
                border-width: 1px;
                padding: 6px;
				background-color: #D4E6F1;
                border-style: solid;
                border-color: #666666;

            }
            table.gridtable td {
                border-width: 1px;
                padding: 8px;
                border-style: solid;
                border-color: #666666;
            }
            .error {
                color: white;
                background-color: red;
            }
        </style>
</head>

<body>   
    <div class="container" id="container">
        <table class="gridtable">
				<form action="exp03.php" method="post"> 
				<h2 style="text-align:center"> Managed Objects Summary </h2>            <!-- shashender -->
			<hr>
            <thead>
                <tr>
                   <th style="text-align:center">Managed Objects<input type="text" name="moSummary"><input type="submit" value="Search"></th> 	
                   <th style="text-align:center">Match</th>
     <!-- comment out               <th>Tags</th>  -->
     <!-- comment out               <th>Manual Template</th>  -->
     <!-- comment out               <th>Auto Template</th>  -->
     <!-- comment out               <th>Automitigation</th>  -->
     <!-- comment out               <th>Fast Flood</th>  -->
					<th style="text-align:center">Shared Detection</th>
     <!-- comment out               <th>Profiled</th>  -->
                </tr>
            </thead>
			</form>
			
		   		<?php

					$mo = $_POST["moSummary"]; 
					
					$d = 1;
					if($mo != null){ $d = $d + 1;}
					if($d == 2){ 				

						function like($str, $searchTerm) {
							$searchTerm = strtolower($searchTerm);
							$str = strtolower($str);
							$pos = strpos($str, $searchTerm);
							if ($pos === false)
								return false;
							else
								return true;
						}

                    if (($csvfile = fopen("mo_summary.csv", "r")) !== FALSE) {					
                        while (($csvdata = fgetcsv($csvfile, 3700, ",")) !== FALSE) {
							if ($csvdata[0] == 'Managed Objects' && $csvdata[1] == 'Match' && $csvdata[2] == 'Tags') {
								while (($csvdata = fgetcsv($csvfile, 3700, ",")) !== FALSE) {
									$found = like($csvdata[0], $mo); //returns true
									$notFound = like($csvdata[0], $mo); //returns false
									echo '<tr>';
									if($found){
										// This will execute only when the text is like the desired string
											echo '<td>'.$csvdata[0].'</td>';
											echo '<td>'.$csvdata[1].'</td>';
											echo '<td><a href="../www/SharedDetection01.php?profileName='.$csvdata[7].'">'.$csvdata[7].'</a></td>';	
									} 
									echo '</tr>';

								}								
							}
						} 
                        fclose($csvfile);
                    }}
                ?>
           
			
			
			        <?php
					$c = 1;
					if($mo != null){ $c = $c + 1;}
					if($c == 1){ 
					
					
                    if (($csvfile = fopen("mo_summary.csv", "r")) !== FALSE) {
                        while (($csvdata = fgetcsv($csvfile, 3700, ",")) !== FALSE) {
							if ($csvdata[0] == 'Managed Objects' && $csvdata[1] == 'Match' && $csvdata[2] == 'Tags') {
								while (($csvdata = fgetcsv($csvfile, 3700, ",")) !== FALSE) {
									$error='';
									$colcount = count($csvdata);
									echo '<tr>';
									if($colcount!=9) {
										$error = 'Column count incorrect';
									}
									

									switch($error) {
										case "Column count incorrect":
											echo '<td></td>';
											echo '<td class="error" >'.$error.'</td>';
											echo '<td></td>';
											break;

										default:
											echo '<td>'.$csvdata[0].'</td>';
											echo '<td>'.$csvdata[1].'</td>';
											echo '<td><a href="../www/SharedDetection01.php?profileName='.$csvdata[7].'">'.$csvdata[7].'</a></td>';
									}
									echo '</tr>';
								}
							}
						}
                        fclose($csvfile);
                    } 
					} 
                ?>


         <!--   </tbody> -->
			</table>



    </div>

</body>
</html>
