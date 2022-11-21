import {
    createApp,
} from 'vue'
import App from './App.vue'

import SmartTable from 'vuejs-smart-table'

import './scss/styles.scss'

createApp(App).use(SmartTable).mount('#app')