export default (context) => {
  const route = context.to.name

  if (route !== ('login' || 'register') && !localStorage.getItem('jwt')) {
    return context.next('/login')
  }
  if (route === ('login' || 'register') && localStorage.getItem('jwt')) {
    return context.next('/home')
  }
}
