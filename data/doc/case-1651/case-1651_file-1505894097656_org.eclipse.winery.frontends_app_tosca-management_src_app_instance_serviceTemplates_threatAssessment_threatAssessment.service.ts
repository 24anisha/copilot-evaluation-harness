/*******************************************************************************
 * Copyright (c) 2018 Contributors to the Eclipse Foundation
 *
 * See the NOTICE file(s) distributed with this work for additional
 * information regarding copyright ownership.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Eclipse Public License 2.0 which is available at
 * http://www.eclipse.org/legal/epl-2.0, or the Apache Software License 2.0
 * which is available at https://www.apache.org/licenses/LICENSE-2.0.
 *
 * SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
 *******************************************************************************/
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { backendBaseURL } from '../../../configuration';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';

@Injectable()
export class ThreatAssessmentService {

    private readonly path: string;

    constructor(private http: HttpClient,
                private route: Router) {
        this.path = this.route.url;

    }

    getThreatData(): Observable<string> {
        const headers = new HttpHeaders({ 'Accept': 'application/json' });

        return this.http.get(
            backendBaseURL + this.path,
            { headers: headers, responseType: 'text' }
        );
    }

}