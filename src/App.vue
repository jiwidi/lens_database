<script setup>

</script>
<template>
  <div class="left">
    <h1>Lens Database filter sidebar</h1>
    <label>Filter by Name:</label>
    <input class="form-control" v-model="filters.name.value" />
    <button class="ui button toggle" @click="() => filters.type.value.push('Zoom')">Filter by Zoom</button>
  </div>
  <div class="container">
    <VTable :data="lenses" :filters="filters">
      <template #head>
        <tr>
          <th>Name</th>
          <th>Mount</th>
          <th>Type</th>
          <th>Max aperture</th>
          <th>Ø filter</th>
        </tr>
      </template>
      <template #body="{ rows }">
        <tr v-for="row in rows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.mount }}</td>
          <td>{{ row.type }}</td>
          <td>{{ row.maxAperture }}</td>
          <td>{{ row.filterSize }}</td>
        </tr>
      </template>
    </VTable>
  </div>
</template>

<script>
import lenses from "./data/lenses.json";

export default {
  name: "main",
  data() {
    return {
      lenses,
      filters: {
        name: { value: "", keys: ["name"] },
        type: { value: [], custom: this.typeFilter }
      }
    }
  },
  methods: {
    typeFilter (filterValue, row) {
      if (filterValue.length === 0) return true
      else  return filterValue.includes(row.type)
    }
  }
}
</script>

<style scoped></style>
