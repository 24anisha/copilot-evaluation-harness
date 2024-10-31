import * as storage from "localforage";
import { getEnv, types } from "mobx-state-tree";

import { getDependencyViews } from "./dependencyViews";

import BottleStore from "./BottleStore";
import EventStore from "./EventStore";
import LocationStore from "./LocationStore";
import MemberStore from "./MemberStore";
import { RouterStore } from "./RouterStore";
import ScotchNightStore from "./ScotchNightStore";

export const RootStore = types
    .model("RootStore", {
        hydrated: false,
        bottleStore: types.optional(BottleStore, {}),
        eventStore: types.optional(EventStore, {}),
        locationStore: types.optional(LocationStore, {}),
        memberStore: types.optional(MemberStore, {}),
        navigation: types.optional(RouterStore, {}),
        scotchNightStore: types.optional(ScotchNightStore, {})
    })
    .views((self) => getDependencyViews(self))
    .actions((self) => {
        function afterHydration() {
            self.hydrated = true;

            const auth = getEnv(self).auth;

            refreshAppData();
        }

        function clear() {
            self.scotchNightStore.clear();
        }

        const refreshAppData = async () => {
            const { bottleStore, eventStore, locationStore, scotchNightStore } = self;
            const { currentUser } = scotchNightStore;

            if (!currentUser) {
                return;
            }

            await bottleStore.loadBottles();
            await locationStore.loadLocations();

            eventStore.loadEventsForMember(currentUser);
        };

        return {
            afterHydration,
            clear,
            refreshAppData
        };
    });

export type IRootStore = typeof RootStore.Type;

export default RootStore;