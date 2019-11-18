// function sortTable(n) {
//   var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
//   table = document.getElementById("dataTable");
//   switching = true;
//   // Set the sorting direction to ascending:
//   dir = "asc";
//   /* Make a loop that will continue until
//   no switching has been done: */
//   while (switching) {
//     // Start by saying: no switching is done:
//     switching = false;
//     rows = table.rows;
//     /* Loop through all table rows (except the
//     first, which contains table headers): */
//     for (i = 1; i < (rows.length - 1); i++) {
//       // Start by saying there should be no switching:
//       shouldSwitch = false;
//       /* Get the two elements you want to compare,
//       one from current row and one from the next: */
//       x = rows[i].getElementsByTagName("TD")[n];
//       y = rows[i + 1].getElementsByTagName("TD")[n];
//       /* Check if the two rows should switch place,
//       based on the direction, asc or desc: */
//       if (dir == "asc") {
//         if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
//           // If so, mark as a switch and break the loop:
//           shouldSwitch = true;
//           break;
//         }
//       } else if (dir == "desc") {
//         if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
//           // If so, mark as a switch and break the loop:
//           shouldSwitch = true;
//           break;
//         }
//       }
//     }
//     if (shouldSwitch) {
//       /* If a switch has been marked, make the switch
//       and mark that a switch has been done: */
//       rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
//       switching = true;
//       // Each time a switch is done, increase this count by 1:
//       switchcount ++;
//     } else {
//       /* If no switching has been done AND the direction is "asc",
//       set the direction to "desc" and run the while loop again. */
//       if (switchcount == 0 && dir == "asc") {
//         dir = "desc";
//         switching = true;
//       }
//     }
//   }
// }

// function goto(){
//   var row;
//   row = 
// }

// $('tr[data-href]').on("click", function() {
//     document.location = $(this).data('href');
// });

// function sortTable(n) {
//   var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
//   table = document.getElementById("dataTable");
//   switching = true;
//   //Set the sorting direction to ascending:
//   dir = "asc"; 
//   /*Make a loop that will continue until
//   no switching has been done:*/
//   while (switching) {
//     //start by saying: no switching is done:
//     switching = false;
//     rows = table.rows;
//     /*Loop through all table rows (except the
//     first, which contains table headers):*/
//     for (i = 1; i < (rows.length - 1); i++) {
//       //start by saying there should be no switching:
//       shouldSwitch = false;
//       /*Get the two elements you want to compare,
//       one from current row and one from the next:*/
//       x = rows[i].getElementsByTagName("TD")[n];
//       y = rows[i + 1].getElementsByTagName("TD")[n];
//       /*check if the two rows should switch place,
//       based on the direction, asc or desc:*/
//       if (dir == "asc") {
//         if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
//           //if so, mark as a switch and break the loop:
//           shouldSwitch= true;
//           break;
//         }
//       } else if (dir == "desc") {
//         if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
//           //if so, mark as a switch and break the loop:
//           shouldSwitch = true;
//           break;
//         }
//       }
//     }
//     if (shouldSwitch) {
//       /*If a switch has been marked, make the switch
//       and mark that a switch has been done:*/
//       rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
//       switching = true;
//       //Each time a switch is done, increase this count by 1:
//       switchcount ++;      
//     } else {
//       /*If no switching has been done AND the direction is "asc",
//       set the direction to "desc" and run the while loop again.*/
//       if (switchcount == 0 && dir == "asc") {
//         dir = "desc";
//         switching = true;
//       }
//     }
//   }
// }

function sortTable(n, arrow_element, el1, el2, el3, el4) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0, arrow;
  table = document.getElementById("dataTable");
  switching = true;
  // Set the sorting direction to ascending:
  dir = "asc";
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */

    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        arrow = document.getElementById(arrow_element);
        arrow.textContent="keyboard_arrow_down";
        document.getElementById(el1).textContent="unfold_more";
        document.getElementById(el2).textContent="unfold_more";
        document.getElementById(el3).textContent="unfold_more";
        document.getElementById(el4).textContent="unfold_more";
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        arrow = document.getElementById(arrow_element);
        arrow.textContent="keyboard_arrow_up";
        document.getElementById(el1).textContent="unfold_more";
        document.getElementById(el2).textContent="unfold_more";
        document.getElementById(el3).textContent="unfold_more";
        document.getElementById(el4).textContent="unfold_more";
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
