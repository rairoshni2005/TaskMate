describe('Add Task', () => {

    it('should add task', () => {

        cy.visit('http://127.0.0.1:5001', {
            failOnStatusCode: false
        })

        cy.wait(3000)

        cy.get('#task-name').type('Cypress Task')

        cy.get('#task-due').type('2026-06-01T18:00')

        cy.get('#task-priority').select('High')

        cy.get('#task-form').submit()

        cy.wait(2000)

        cy.get('#task-list')
          .should('contain', 'Cypress Task')

    })

})