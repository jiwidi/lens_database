import {
    createApp,
} from 'vue'
import App from './App.vue'

import SmartTable from 'vuejs-smart-table'

import './assets/main.css'


createApp(App).use(SmartTable).mount('#app')