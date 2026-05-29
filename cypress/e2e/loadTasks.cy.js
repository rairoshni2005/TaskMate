describe('Load Tasks', () => {

    it('should load tasks', () => {

        cy.visit('http://127.0.0.1:5001')

        cy.get('#task-list li')
          .should('exist')

    })
})