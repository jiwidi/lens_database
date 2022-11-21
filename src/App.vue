<script setup>

</script>
<template>
  <div class="app-wrapper">
    <div class="sidebar">
      <h1>Lens Database filter sidebar</h1>
      <label>Filter by Name:</label>
      <input class="form-control" v-model="filters.name.value" />
      <button class="ui button toggle" @click="filters.type.value.push('Zoom')">Filter by Zoom</button>
      <ToggleButton @click="pishita(filters, 'type', 'Zoom', $event.target)">Hello</ToggleButton>
    </div>
    <div class="content">
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
  </div>
</template>

<script>
import lenses from './data/lenses.json'
import ToggleButton from './components/ToggleButton.vue'

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
      else return filterValue.includes(row.type)
    },

    pishita (filters, field, value, button) {
      button.isActive = this.isActive ? false : true
      console.log(button.isActive)
      filters[field].value.push(value)
    }
  },

  components: {
    ToggleButton,
  }
}
</script>

<style scoped></style>
