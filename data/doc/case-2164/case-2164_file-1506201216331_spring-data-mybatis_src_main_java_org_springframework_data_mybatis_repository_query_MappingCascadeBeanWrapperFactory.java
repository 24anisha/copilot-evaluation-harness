/*
 * Copyright 2012-2019 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.springframework.data.mybatis.repository.query;

import java.util.Map;
import java.util.Optional;

import org.springframework.data.mapping.context.PersistentEntities;
import org.springframework.util.Assert;
import org.springframework.util.ConcurrentReferenceHashMap;

/**
 * .
 *
 * @author JARVIS SONG
 * @since 2.0.2
 */
public class MappingCascadeBeanWrapperFactory implements CascadeBeanWrapperFactory {

	private final PersistentEntities entities;

	private final Map<Class<?>, MappingCascadeMetadata> metadataCache;

	public MappingCascadeBeanWrapperFactory(PersistentEntities entities) {

		Assert.notNull(entities, "PersistentEntities must not be null!");

		this.entities = entities;
		this.metadataCache = new ConcurrentReferenceHashMap<>();
	}

	@Override
	public <T> Optional<CascadeBeanWrapper<T>> getBeanWrapperFor(T source) {
		return Optional.of(source)
				.flatMap(it -> this.entities
						.mapOnContext(it.getClass(),
								(context, entities) -> Optional
										.<CascadeBeanWrapper<T>>ofNullable(new MappingMetadataCascadeBeanWrapper<>()))
						.orElseGet(null));
	}

	static class MappingCascadeMetadata {

	}

	static class MappingMetadataCascadeBeanWrapper<T> implements CascadeBeanWrapper<T> {

	}

}