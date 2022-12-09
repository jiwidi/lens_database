<script setup>

</script>
<template>
  <div class="app-wrapper">
    <div class="sidebar">
      <h1>Lens Database</h1>
      <button @click="runSql('SELECT * FROM lenses')">
        SELECT * FROM mytable
      </button>

       <pre>{{ result }}</pre>
      <h2>Filter by Name:</h2>
      <input class="form-control" v-model="filters.name.value" />
      <h2>Type</h2>
      <div class="button-group">
        <FilterButton @update-filter="(action) => pishita('type', 'Zoom', action)">Zoom</FilterButton>
        <FilterButton @update-filter="(action) => pishita('type', 'Prime', action)">Prime</FilterButton>
      </div>
      <h2>Aperture</h2>
      <div class="button-group">
        <FilterButton v-for="aperture in apertures" :key="aperture" @update-filter="(action) => pishita('aperture', aperture, action)">{{ aperture }}</FilterButton>
      </div>
    </div>
    <div class="content">
      <VTable :data="lenses" :filters="filters">
        <template #head>
          <tr>
            <th>Name</th>
            <th>Mount</th>
            <th>Type</th>
            <th>Max aperture</th>
          </tr>
        </template>
        <template #body="{ rows }">
          <tr v-for="row in rows" :key="row.name">
            <td>{{ row.name }}</td>
            <td>{{ row.mount }}</td>
            <td>{{ row.type }}</td>
            <td>F/{{ row.max_aperture }}</td>
          </tr>
        </template>
      </VTable>
      <smart-pagination
        :currentPage.sync="currentPage"
        :pageSize="pageSize"
      />
    </div>
  </div>
</template>

<script>
import lenses from './data/lenses_big.json'
import FilterButton from './components/FilterButton.vue'
import { createDbWorker } from "sql.js-httpvfs";

const publicPath = "/";
const workerUrl = new URL(
  "sql.js-httpvfs/dist/sqlite.worker.js",
  import.meta.url,
);
const wasmUrl = new URL(
  "sql.js-httpvfs/dist/sql-wasm.wasm",
  import.meta.url,
);

export default {
  name: "main",
  data() {
    return {
      lenses,
      currentPage: 1,
      pageSize: 30,
      apertures: null,
      filters: {
        name: { value: "", keys: ["name"] },
        type: { value: [], custom: this.typeFilter },
        aperture: { value: [], custom: this.apertureFilter }
      }
    }
  },

  async mounted () {
    this.apertures = [...new Set(this.lenses.map(lens => lens.max_aperture))];
    this.worker = await createDbWorker(
      [
        {
          from: "inline",
          config: {
            serverMode: "full",
            url: `${publicPath}db/lenses.db`,
            requestChunkSize: 4096,
          },
        },
      ],
      workerUrl.toString(),
      wasmUrl.toString()
    );
  },

  methods: {
    typeFilter (filterValue, row) {
      if (filterValue.length === 0) return true
      else return filterValue.includes(row.type)
    },

    apertureFilter (filterValue, row) {
      if (filterValue.length === 0) return true
      else return filterValue.includes(row.max_aperture)
    },

    pishita (field, value, action) {
      action === 'add' ? this.filters[field].value.push(value) : this.filters[field].value.pop(value)
    },

    async runSql(sql) {
      this.result = await this.worker.db.query(sql);
      console.log(this.result);
    },
  },

  components: {
    FilterButton,
  }
}
</script>

<style scoped></style>
