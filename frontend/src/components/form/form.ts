import type {ComponentType} from "./types.ts";

export interface FormSchema {
    field: string;
    label: string;
    component: ComponentType;
    show?: boolean;
}
