describe('Filter Tasks', () => {

    it('should filter tasks', () => {

        cy.visit('http://127.0.0.1:5001')

        cy.window().then((win) => {
            win.filterTasks('High')
        })

    })
})