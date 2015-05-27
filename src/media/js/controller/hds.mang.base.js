var managementApp=angular.module('managementApp',[]);
managementApp.controller('managementCtrl',['$scope',function($scope,$modal){
    $scope.changeLeftPanelStatus=function(index){
        $scope.leftPanelStatus[index]=!$scope.leftPanelStatus[index];
        if($scope.leftPanelStatus[index]==true){
            for(i=0;i<$scope.leftPanelStatus.length;i++){
                if(i!=index){
                    $scope.leftPanelStatus[i]=false;
                }
            }
        }
    }
}])
managementApp.controller('loginCtrl',['$scope',function($scope){

}])
