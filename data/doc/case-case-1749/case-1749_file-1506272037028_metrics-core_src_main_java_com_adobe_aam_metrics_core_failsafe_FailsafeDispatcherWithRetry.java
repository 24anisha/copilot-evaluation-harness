/*
 * Copyright 2018 Adobe Systems Incorporated. All rights reserved.
 * This file is licensed to you under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License. You may obtain a copy
 * of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under
 * the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
 * OF ANY KIND, either express or implied. See the License for the specific language
 * governing permissions and limitations under the License.
 *
 */
package com.adobe.aam.metrics.core.failsafe;

import com.adobe.aam.metrics.core.publish.PublishCommand;
import net.jodah.failsafe.Failsafe;
import net.jodah.failsafe.RetryPolicy;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Responsible for publishing metrics to the Graphite Backend using a configured retry mechanism
 * provided by Failsafe.
 *
 * References:
 * - https://github.com/jhalterman/failsafe
 */
public class FailsafeDispatcherWithRetry implements FailsafeDispatcher {
    private static final Logger logger = LoggerFactory.getLogger(FailsafeDispatcherWithRetry.class);

    private final RetryPolicy retryPolicy;

    public FailsafeDispatcherWithRetry(RetryPolicy retryPolicy) {
        this.retryPolicy = retryPolicy;
    }

    @Override
    public void dispatch(final PublishCommand publishCommand) {
        try {
            Failsafe.with(retryPolicy).run(publishCommand::execute);
        } catch (Exception e) {
            logger.warn("Failed to publish metrics to Graphite.", e.getMessage());
        }
    }
}