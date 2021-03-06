/**
 * Copyright 2017 Ent. Services Development Corporation LP
 *
 * @fileOverview Create Bucket JS
 * @requires AngularJS and jQuery
 *
 */
angular.module('CreateBucketModule', ['ModalModule', 'EucaConsoleUtils', 'BucketServiceModule'])
.directive('createBucketDialog', function() {
    return {
        restrict: 'A',
        scope: {
            bucketName: '='
        },
        templateUrl: '/_template/dialogs/create_bucket_dialog2',
        controller: ['$scope', '$http', '$timeout', 'eucaHandleError', 'ModalService', 'BucketService', 
        function ($scope, $http, $timeout, eucaHandleError, ModalService, BucketService) {
            var vm = this;
            $http.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
            vm.existingBucketConflict = false;
            vm.isCreatingBucket = false;
            vm.bucketName = '';
            vm.handleCreateBucket = function ($event) {
                $event.preventDefault();
                if ($scope.createBucketForm.$invalid) {
                    return false;
                }
                vm.isCreatingBucket = true;
                BucketService.createBucket(vm.bucketName, $('#csrf_token').val()).then(
                    function success(oData) {
                        $scope.bucketName = vm.bucketName;
                        // this was tricky to get working. $apply() needs to be called, but wasn't
                        // returning, so wrapping clean up calls in timeout function to ensure they're called after.
                        $timeout(function() {
                            vm.isCreatingBucket = false;
                            ModalService.closeModal('createBucketDialog');
                        });
                        $scope.$apply();
                    },
                    function error(oData) {
                        eucaHandleError(oData);
                        vm.isCreatingBucket = false;
                    }
                );
            };
        }],
        controllerAs: 'createBucket'
    };
});
