angular.module('myApp', [])
  .controller('myController', function($scope) {
    $scope.myArray = pname;
    $scope.myArray2 = pid;
});

angular.element(document).ready(function() {
  angular.bootstrap(document, ['myApp']);
});

function validate() { 
	var g = document.getElementById("accept").required; 
        document.getElementById("sudo").innerHTML = g; 
        } 

