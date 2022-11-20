<template>
    <button :class="{active:isActive}"
      >
      <slot />
    </button>
  </template>

  <script>
  export default {
    name: 'togglebutton',
    props: {
      type: {
        type: String,
        default: 'save',
      },
    },
    data () {
      return {
        active: false,
      }
    },
    methods: {
  },
  };
  </script>