<script setup>
</script>

<template>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <v-table :data="users">
      <thead slot="head">
          <th>Name</th>
          <th>Age</th>
      </thead>
      <tbody slot="body" slot-scope="{displayData}">
          <tr v-for="row in displayData" :key="row.id">
            <td>{{ row.id }}</td>
            <td>{{ row.title }}</td>
          </tr>
      </tbody>
    </v-table>
  </template>

<script>
import users from './data/karaoke.json'

export default {
    name: 'users',
    data: () => ({
        users
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
