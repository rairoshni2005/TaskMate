describe('Delete Task', () => {

    it('should delete task', () => {

        cy.visit('http://127.0.0.1:5001')

        cy.contains('Delete').click()

    })
})