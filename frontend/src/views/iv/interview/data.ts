import type {BasicColumn} from "../../../components/table/table.ts";
import type {FormSchema} from "../../../components/form/form.ts";

export const columns: BasicColumn[] = [
    {
        label: '名称',
        prop: 'name',
    }
]

export const formSchema: FormSchema[] = [
    {
        field: 'id',
        label: '',
        component: 'Input',
        show: false,
    },
    {
        field: 'name',
        label: '名称',
        component: 'Input',
    },
]
