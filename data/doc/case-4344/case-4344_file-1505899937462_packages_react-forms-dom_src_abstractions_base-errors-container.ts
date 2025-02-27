import * as Immutable from "immutable";
import { BaseContainer, BaseContainerParentContext } from "@simplr/react-forms";
import { FormStore } from "@simplr/react-forms/stores";
import { FormError, FieldValidationStatus } from "@simplr/react-forms/contracts";

export type BaseErrorsContainerProps = {};

export type FieldErrors = Immutable.Map<string, FormError>;

export interface BaseErrorsContainerState {
    FieldErrors: FieldErrors;
    FormError?: FormError;
}

export abstract class BaseErrorsContainer<TProps extends BaseErrorsContainerProps, TState extends BaseErrorsContainerState>
    extends BaseContainer<TProps, TState> {
    public state: TState = {
        FieldErrors: Immutable.Map<string, FormError>()
    } as TState;

    protected OnStoreUpdated(): void {
        const storeState = this.FormStore.GetState();

        if (!storeState.HasError) {
            this.setState(state => {
                state.FieldErrors = Immutable.Map<string, FormError>();
                state.FormError = undefined;
                return state;
            });
            return;
        }
        const formError = storeState.Form.Error;
        const fieldsWithError = storeState
            .FieldsValidationStatuses
            .filter(x => x != null && x === FieldValidationStatus.HasError)
            .keySeq()
            .toArray();

        const fieldsErrors: { [id: string]: FormError } = {};

        fieldsWithError.forEach(fieldId => {
            const fieldError = storeState.Fields.get(fieldId).Error;
            if (fieldError != null) {
                fieldsErrors[fieldId] = fieldError;
            }
        });

        this.setState(state => {
            state.FormError = formError;
            state.FieldErrors = Immutable.Map<string, FormError>(fieldsErrors);

            return state;
        });
    }

    public abstract render(): JSX.Element | null;
}