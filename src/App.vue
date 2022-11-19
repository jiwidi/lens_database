<script setup>
</script>

<template>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <v-table :data="lenses">
 <template #head>
   <thead slot="head">
     <th>Name</th>
     <th>mount</th>
   </thead>
 </template>
 <template #body="{ rows }">
   <tbody>
     <tr v-for="row in rows" :key="row.name">
       <td>{{ row.name }}</td>
       <td>{{ row.mount }}</td>
     </tr>
   </tbody>
 </template>
</v-table>
  </template>

<script>
import lenses from './data/lenses.json'

export default {
    name: 'main',
    data: () => ({
        lenses
    })
}
</script>


<style scoped>
header {
    line-height: 1.5;
}

.logo {
    display: block;
    margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
    header {
        display: flex;
        place-items: center;
        padding-right: calc(var(--section-gap) / 2);
    }

    .logo {
        margin: 0 2rem 0 0;
    }

    header .wrapper {
        display: flex;
        place-items: flex-start;
        flex-wrap: wrap;
    }
}
</style>
