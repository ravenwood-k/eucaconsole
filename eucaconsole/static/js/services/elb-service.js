/**
 * Copyright 2016 Hewlett Packard Enterprise Development LP
 *
 * @fileOverview factory method for elb XHR calls
 * @requires AngularJS
 *
 */
angular.module('ELBServiceModule', [])
.factory('ELBService', ['$http', function ($http) {
    $http.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    return {
        createELB: function (csrfToken, values) {
            var data = {
                csrf_token: csrfToken,
                name: values.elbName,
                elb_listener: values.listeners.map(function(val) { return JSON.stringify(val); }),
                vpc_network: values.vpcNetwork.id,
                vpc_subnet: values.vpcSubnets.map(function(val) { return val.id; }),
                securitygroup: values.vpcSecurityGroups.map(function(val) { return val.id; }),
                zone: values.availabilityZones.map(function(val) { return val.id; }),
                cross_zone_enabled: values.crossZoneEnabled,
                ping_protocol: values.pingProtocol,
                ping_port: values.pingPort,
                ping_path: values.pingPath,
                response_timeout: values.responseTimeout,
                time_between_pings: values.timeBetweenPings,
                failures_until_unhealthy: values.failuresUntilUnhealthy,
                passes_until_healthy: values.passesUntilHealthy,
                logging_enabled: values.loggingEnabled,
                bucket_name: values.bucketName,
                bucket_prefix: values.bucketPrefix,
                collection_interval: values.collectionInterval
            };
            return $http({
                method: 'POST',
                url: '/elbs/create',
                data: $.param(data, true),
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(function success (response) {
                var data = response.data || {
                    results: []
                };
                return data.results;
            });
        }
    };
}]);
