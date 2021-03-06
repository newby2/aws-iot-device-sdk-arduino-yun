'''
/*
 * Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

import operationTimeoutException
import operationError

# Serial Exception
class acceptTimeoutException(Exception):
    def __init__(self, msg="Accept Timeout"):
        self.message = msg

# MQTT Operation Timeout Exception
class connectTimeoutException(operationTimeoutException.operationTimeoutException):
    def __init__(self, msg="Connect Timeout"):
        self.message = msg

class disconnectTimeoutException(operationTimeoutException.operationTimeoutException):
    def __init__(self, msg="Disconnect Timeout"):
        self.message = msg

class publishTimeoutException(operationTimeoutException.operationTimeoutException):
    def __init__(self, msg="Publish Timeout"):
        self.message = msg

class subscribeTimeoutException(operationTimeoutException.operationTimeoutException):
    def __init__(self, msg="Subscribe Timeout"):
        self.message = msg

class unsubscribeTimeoutException(operationTimeoutException.operationTimeoutException):
    def __init__(self, msg="Unsubscribe Timeout"):
        self.message = msg

# MQTT Operation Error
class connectError(operationError.operationError):
    def __init__(self, errorCode):
        self.message = "Connect Error: " + str(errorCode)

class disconnectError(operationError.operationError):
    def __init__(self, errorCode):
        self.message = "Disconnect Error: " + str(errorCode)

class publishError(operationError.operationError):
    def __init__(self, errorCode):
        self.message = "Publish Error: " + str(errorCode)

class subscribeError(operationError.operationError):
    def __init__(self, errorCode):
        self.message = "Subscribe Error: " + str(errorCode)

class unsubscribeError(operationError.operationError):
    def __init__(self, errorCode):
        self.message = "Unsubscribe Error: " + str(errorCode)
